import { Component, inject } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { CommonModule } from '@angular/common'
import { Navbar } from '../navbar/navbar';
import { FarmersByCrop } from '../farmers-by-crop/farmers-by-crop';
import { AddRole } from '../add-role/add-role';
import { RemoveRole } from '../remove-role/remove-role';
import { Getbill } from '../getbill/getbill';
import { Farmers } from '../farmers/farmers';
import { Farms } from '../farms/farms';
import { Schedules } from '../schedules/schedules';
import { SchedulesDue } from '../schedules-due/schedules-due';
import { CreateSchedule } from '../create-schedule/create-schedule';
import { CreateFarm } from '../create-farm/create-farm';
import { CreateFarmer } from '../create-farmer/create-farmer';
import { FarmersWithCrop } from '../farmers-with-crop/farmers-with-crop';


@Component({
  selector: 'app-home',
  standalone: true,
  imports: [[CommonModule, Navbar, FarmersByCrop, FarmersWithCrop, AddRole, RemoveRole, Getbill, Farmers, Farms, Schedules, SchedulesDue, CreateSchedule, CreateFarm,CreateFarmer]],
  templateUrl: './home.html',
  styleUrl: './home.css'
})
export class Home {
  user$ = inject(AuthService).user$;
  activeView: string = 'welcome';

  setView(view: string): void {
    this.activeView = view;
  }
}
