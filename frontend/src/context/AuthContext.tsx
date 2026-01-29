import { createContext, useContext, useState, ReactNode } from "react"
import { api } from "@/services/api"

interface AuthContextType {
  isAuthenticated: boolean
  login: (email: string, password: string) => Promise<void>
  logout: () => void
}

const AuthContext = createContext<AuthContextType | undefined>(undefined)

export function AuthProvider({ children }: { children: ReactNode }) {
  const [isAuthenticated, setIsAuthenticated] = useState(
    !!localStorage.getItem("access")
  )

  const login = async (email: string, password: string) => {
    const data = await api.login(email, password)

    localStorage.setItem("access", data.access)
    localStorage.setItem("refresh", data.refresh)

    setIsAuthenticated(true)
  }

  const logout = () => {
    localStorage.removeItem("access")
    localStorage.removeItem("refresh")
    setIsAuthenticated(false)
  }

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth() {
  const context = useContext(AuthContext)
  if (!context) {
    throw new Error("useAuth must be used within AuthProvider")
  }
  return context
}
