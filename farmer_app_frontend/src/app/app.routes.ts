import { Routes } from '@angular/router';
import { Register } from './components/register/register';
import { Login } from './components/login/login';
import { Home } from './components/home/home';
import { AuthGuard } from './gaurds/auth.gaurd';

export const routes: Routes = [
    {path: 'login', component: Login},
    {path: 'register', component: Register},
    {path: 'home', component: Home, canActivate: [AuthGuard]},
    {path: '', redirectTo: 'home', pathMatch: 'full'}
];
