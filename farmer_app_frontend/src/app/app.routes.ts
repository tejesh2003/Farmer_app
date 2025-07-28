import { Routes } from '@angular/router';
import { Register } from './components/register/register';
import { Login } from './components/login/login';
import { Home } from './components/home/home';
import { AuthGuard } from './gaurds/auth.gaurd';
import { CreateFarm } from './components/create-farm/create-farm';
import { CreateSchedule } from './components/create-schedule/create-schedule';
import { RoleGuard } from './gaurds/role.gaurd';

export const routes: Routes = [
    {path: 'login', component: Login},
    {path: 'register', component: Register},
    {path: 'home', component: Home, canActivate: [AuthGuard]},
    {path: '', redirectTo: 'home', pathMatch: 'full'},
    {path: 'create-farm/:id',component: CreateFarm ,canActivate: [AuthGuard, RoleGuard]},
    {path: 'create-schedule/:id',component: CreateSchedule,canActivate: [AuthGuard, RoleGuard]}

];
