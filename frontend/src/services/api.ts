const BASE_URL = "http://127.0.0.1:8000/api"

export const api = {
  async login(email: string, password: string) {
    const response = await fetch(`${BASE_URL}/token/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    })

    if (!response.ok) {
      throw new Error("Login failed")
    }

    return response.json() // returns { access, refresh }
  },

  async authenticatedFetch(url: string, options: RequestInit = {}) {
    const token = localStorage.getItem("access")

    return fetch(`${BASE_URL}${url}`, {
      ...options,
      headers: {
        "Content-Type": "application/json",
        Authorization: token ? `Bearer ${token}` : "",
        ...options.headers,
      },
    })
  },
}
