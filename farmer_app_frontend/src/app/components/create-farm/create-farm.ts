import { ChangeDetectorRef, Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { FarmService } from '../../services/farm.service';

@Component({
  selector: 'app-create-farm',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './create-farm.html',
  styleUrl: './create-farm.css'
})
export class CreateFarm {
  farmForm: FormGroup;
  success = false;

  constructor(private fb: FormBuilder, private farmService: FarmService, private cdr: ChangeDetectorRef) {
    this.farmForm = this.fb.group({
      village: ['', Validators.required],
      sowing_date: ['', Validators.required],
      area: [null, [Validators.required, Validators.min(0.1)]],
      crop: ['', Validators.required],
      farmer_id: [null, Validators.required]
    });
  }

  submit(): void {
    if (this.farmForm.invalid) return;

    this.farmService.createFarm(this.farmForm.value).subscribe({
      next: () => {
        this.success = true,
        this.cdr.detectChanges();
        this.farmForm.reset();
      },
      error: err => console.error('Failed to create farm:', err)
    });
  }
}
