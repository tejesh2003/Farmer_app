import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, FormGroup, FormArray, Validators } from '@angular/forms';
import { BillService } from '../../services/bill.service';
import { FarmerBill } from '../../models/models';
import { ChangeDetectorRef } from '@angular/core';

@Component({
  selector: 'app-getbill',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './getbill.html',
  styleUrl: './getbill.css'
})
export class Getbill {
  billForm: FormGroup;
  billData: FarmerBill | null = null;

  constructor(private fb: FormBuilder, private billService: BillService, private cdr: ChangeDetectorRef) {
    this.billForm = this.fb.group({
      farmerId: ['', Validators.required],
      fertilizers: this.fb.array([this.createFertilizerGroup()])
    });
  }

  get fertilizers(): FormArray {
    return this.billForm.get('fertilizers') as FormArray;
  }

  createFertilizerGroup(): FormGroup {
    return this.fb.group({
      name: ['', Validators.required],
      unit: ['kg', Validators.required],
      price: [0, [Validators.required, Validators.min(0)]]
    });
  }

  addFertilizer(): void {
    this.fertilizers.push(this.createFertilizerGroup());
  }

  getBill(): void {
  const { farmerId, fertilizers } = this.billForm.value;

  const fertilizerPrices: { [key: string]: number } = {};
  fertilizers.forEach((f: { name: string; unit: string; price: number }) => {
    const key = `${f.name}_${f.unit}`;
    fertilizerPrices[key] = f.price;
  });

  this.billService.getBill(farmerId, fertilizerPrices).subscribe({
    next: data => (
      this.billData = data,
      this.cdr.detectChanges()
    ),
    error: err => console.error('Failed to fetch bill:', err)
  });
}


}
