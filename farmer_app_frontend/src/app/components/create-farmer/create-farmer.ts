import { ChangeDetectorRef, Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { FarmerService } from '../../services/farmer.service';

@Component({
  selector: 'app-create-farmer',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './create-farmer.html',
  styleUrl: './create-farmer.css'
})
export class CreateFarmer {
  farmerForm: FormGroup;
  success = false;

  constructor(private fb: FormBuilder, private farmerService: FarmerService, private cdr: ChangeDetectorRef) {
    this.farmerForm = this.fb.group({
      name: ['', Validators.required],
      phone: ['', [Validators.required, Validators.pattern(/^\d{10}$/)]],
      language: ['', Validators.required],
      country: ['', Validators.required] 
    });
  }

  submit(): void {
    if (this.farmerForm.invalid) return;

    this.farmerService.createFarmer(this.farmerForm.value).subscribe({
      next: () => {
        this.success = true,
        this.cdr.detectChanges();
        this.farmerForm.reset();
      },
      error: (err) => console.error('Failed to create farmer:', err)
     });

  }
}
