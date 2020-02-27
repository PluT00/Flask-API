import React, {useState} from 'react'
import {useHttp} from "../hooks/http.hook";

export const AuthPage = () => {
  const {loading, error, request} = useHttp()
  const [form, setForm] = useState({
    username: '', password: ''
  })

  const changeHandler = event => {
    setForm({ ...form, [event.target.name]: event.target.value })
  }

  const authHandler = async () => {
    try {
      const data = await request('/api/token/', 'POST', {...form})
      console.log(data)
    } catch (e) {}
  }

  return (
      <div className="row justify-content-center mt-5">
        <div className="col-sm-4">
          <form>
            <div className="form-group">
              <label htmlFor="username">Username</label>
              <input
                  type="username"
                  className="form-control"
                  id="username"
                  placeholder="Enter username"
                  onChange={changeHandler}
              />
            </div>
            <div className="form-group">
              <label htmlFor="password">Password</label>
              <input
                  type="password"
                  className="form-control"
                  id="password"
                  placeholder="Enter password"
                  onChange={changeHandler}
              />
            </div>
            <button
                type="submit"
                className="btn btn-primary"
                onClick={authHandler}
                disabled={loading}
            >
              Login
            </button>
          </form>
        </div>
      </div>
  )
}
