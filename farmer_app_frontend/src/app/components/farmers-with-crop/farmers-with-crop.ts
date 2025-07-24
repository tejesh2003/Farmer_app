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
  farmers: Farmer[] = [];
  loading = true;

  constructor(private farmerService: FarmerService, private cdr: ChangeDetectorRef) {}

  ngOnInit(): void {
    this.farmerService.getFarmersWithCrop().subscribe({
      next: (res) => {
        this.farmers = res;
        this.loading = false;
        this.cdr.detectChanges();
      },
      error: (err) => {
        console.error('Failed to fetch farmers:', err);
        this.loading = false;
      }
    });
  }
}
