import { Component, inject } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { CommonModule } from '@angular/common'
import { Navbar } from '../navbar/navbar';
import { FarmersByCrop } from '../farmers-by-crop/farmers-by-crop';
import { AddRole } from '../add-role/add-role';
import { RemoveRole } from '../remove-role/remove-role';
import { Getbill } from '../getbill/getbill';
import { SchedulesDue } from '../schedules-due/schedules-due';
import { CreateFarmer } from '../create-farmer/create-farmer';
import { FarmersWithCrop } from '../farmers-with-crop/farmers-with-crop';
import { AllFarmers } from '../all-farmers/all-farmers';
import { AllUsers } from '../all-users/all-users';
import { CreateCountry } from '../create-country/create-country';


@Component({
  selector: 'app-home',
  standalone: true,
  imports: [[CommonModule, Navbar, FarmersByCrop, FarmersWithCrop, AddRole, RemoveRole, Getbill, SchedulesDue,CreateFarmer, AllFarmers, AllUsers, CreateCountry]],
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
