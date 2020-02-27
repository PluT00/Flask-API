import React, {useState} from 'react'
import {useHttp} from "../hooks/http.hook"
import {NavLink} from "react-router-dom"

export const RegisterPage = () => {
    const {loading, error, request} = useHttp()
    const [form, setForm] = useState({
        username: '', password: '', email: '', first_name: '', last_name: ''
    })

    const changeHandler = event => {
        return setForm({ ...form, [event.target.name]: event.target.value })
    }

    const registerHandler = async () => {
        try {
            const data = await request('api/users/create/', 'POST', {...form})
        } catch (e) {}
    }

  return (
      <div className="row justify-content-center mt-5">
          <div className="col-sm-4">
              <form>
                  <div className="form-group">
                      <label htmlFor="username">Username</label>
                      <input
                          name="username"
                          className="form-control"
                          id="username"
                          placeholder="Enter username"
                          onChange={changeHandler}
                      />
                  </div>
                  <div className="form-group">
                      <label htmlFor="email">Email</label>
                      <input
                          name="email"
                          type="email"
                          className="form-control"
                          id="email"
                          placeholder="ex@mple.com"
                          onChange={changeHandler}
                      />
                  </div>
                  <div className="form-group">
                      <label htmlFor="firstName">First name</label>
                      <input
                          name="first_name"
                          className="form-control"
                          id="firstName"
                          placeholder="First name"
                          onChange={changeHandler}
                      />
                  </div>
                  <div className="form-group">
                      <label htmlFor="lastName">Last name</label>
                      <input
                          name="last_name"
                          className="form-control"
                          id="lastName"
                          placeholder="Last name"
                          onChange={changeHandler}
                      />
                  </div>
                  <div className="form-group">
                      <label htmlFor="password">Password</label>
                      <input
                          name="password"
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
                      onClick={registerHandler}
                      disabled={loading}
                  >
                      Register
                  </button>
                  <NavLink to="/auth" className="btn btn-secondary mx-3">Login</NavLink>
              </form>
          </div>
      </div>
  )
}
