import React from 'react'
import {Switch, Route, Redirect} from 'react-router-dom'
import {ProfilePage} from './pages/ProfilePage'
import {DialogsListPage} from './pages/DialogsListPage'
import {DialogPage} from './pages/DialogPage'
import {FriendsPage} from './pages/FriendsPage'
import {PersonPage} from './pages/PersonPage'
import {AuthPage} from './pages/AuthPage'
import {RegisterPage} from './pages/RegisterPage'

export const useRoutes = isAuthenticated => {
  if (isAuthenticated) {
    return (
      <Switch>
        <Route path='/profile' exact>
          <ProfilePage />
        </Route>
        <Route path='/dialogs' exact>
          <DialogsListPage />
        </Route>
        <Route path='/dialogs/:id'>
          <DialogPage />
        </Route>
        <Route path='/friends' exact>
          <FriendsPage />
        </Route>
        <Route path='/person/:id'>
          <PersonPage />
        </Route>
        <Redirect to="/profile" />
      </Switch>
    )
  }

  return (
    <Switch>
      <Route path='/auth' exact>
        <AuthPage />
      </Route>
      <Route path='/register' exact>
        <RegisterPage />
      </Route>
      <Redirect to="/auth" />
    </Switch>
  )
}
