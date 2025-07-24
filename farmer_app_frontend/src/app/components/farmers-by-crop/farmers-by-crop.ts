import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { Farmer } from '../../models/models';
import { FarmerService } from '../../services/farmer.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-farmers-by-crop',
  standalone:true,
  imports: [CommonModule,FormsModule],
  templateUrl: './farmers-by-crop.html',
  styleUrl: './farmers-by-crop.css'
})
export class FarmersByCrop {
  crop: string='';
  farmers: Farmer[]=[];
  cropTouched: boolean=false;
  isLoading= false;

  constructor(private farmerService: FarmerService, private cdr:ChangeDetectorRef){}

  getFarmersByCrop(): void {
    this.cropTouched=true;
    this.isLoading=true;
    if(this.crop.trim()===''){
        this.isLoading=false;
        this.cdr.detectChanges();
        return;
    }

    this.farmerService.getFarmersByCrop(this.crop).subscribe({
      next : (data)=>{
        this.farmers=data;
        this.isLoading=false;
        this.cdr.detectChanges();
        console.log('Received farmers:', this.farmers); 
      },
      error: (err) => {
        console.error('Failed to fetch farmers by crop', err);
        this.farmers = [];
        this.isLoading=false;
      }
    });
  }

  resetCropSearch():void{
    this.cropTouched=false;
    this.crop='';
    this.farmers=[];
    this.isLoading=false;
  }

}
