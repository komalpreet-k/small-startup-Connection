import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
// username: komalpreet, email komal4443@gmail.com pass: Winnipeg

export default function Login() {
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="w-full max-w-sm bg-white p-6 rounded-xl shadow-md space-y-4">
        <h1 className="text-xl font-bold text-center">Login</h1>

        <Input
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <Input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <Button className="w-full">
          Sign In
        </Button>
      </div>
    </div>
  )
}
