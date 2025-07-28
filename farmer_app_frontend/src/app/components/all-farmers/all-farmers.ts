import {
  Component,
  OnInit,
  ChangeDetectorRef,
  inject
} from '@angular/core';
import { CommonModule } from '@angular/common';
import { FarmerService } from '../../services/farmer.service';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-all-farmers',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './all-farmers.html',
  styleUrls: ['./all-farmers.css']
})
export class AllFarmers implements OnInit {
  farmers: any[] = [];
  selectedFarmer: any = null;
  showPopup: boolean = false;

  showScheduleForm: boolean = false;
  selectedFarmId: number | null = null;

  user$ = inject(AuthService).user$;

  constructor(
    private farmerService: FarmerService,
    private cdr: ChangeDetectorRef,
    private router: Router
  ) {}

  ngOnInit() {
    this.farmerService.getAllFarmers().subscribe(data => {
      this.farmers = data;
      this.cdr.detectChanges();
    });
  }

  openPopup(farmer: any) {
    this.selectedFarmer = farmer;
    this.showPopup = true;
    this.cdr.detectChanges();
  }

  closePopup() {
    this.showPopup = false;
    this.selectedFarmer = null;
    this.showScheduleForm = false;
    this.selectedFarmId = null;
    this.cdr.detectChanges();
  }

  toggleFarmForm() {
  if (!this.selectedFarmer) return;

  const farmerId = this.selectedFarmer.id;
  this.closePopup();
  this.router.navigate(['/create-farm', farmerId]);
}


  toggleScheduleForm(farmId: number) {
  this.closePopup();
  this.router.navigate(['/create-schedule', farmId]);
}

}
