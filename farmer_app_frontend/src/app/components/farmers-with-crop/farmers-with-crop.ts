import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FarmerService } from '../../services/farmer.service';
import { Farmer } from '../../models/models';

@Component({
  selector: 'app-farmers-with-crop',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './farmers-with-crop.html',
  styleUrl: './farmers-with-crop.css'
})
export class FarmersWithCrop implements OnInit {
   farmers: any[] = [];
  selectedFarmer: any = null;
  showPopup: boolean = false;

  constructor(
    private farmerService: FarmerService,
    private cdr: ChangeDetectorRef,
  ) {}

  ngOnInit() {
    this.farmerService.getFarmersWithCrop().subscribe(data => {
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
    this.cdr.detectChanges();
  }

}
