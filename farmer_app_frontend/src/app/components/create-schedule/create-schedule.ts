import { ChangeDetectorRef, Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ScheduleService } from '../../services/schedule.service';

@Component({
  selector: 'app-create-schedule',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './create-schedule.html',
  styleUrl: './create-schedule.css'
})
export class CreateSchedule {
  scheduleForm: FormGroup;
  success = false;

  constructor(private fb: FormBuilder, private scheduleService: ScheduleService, private cdr:ChangeDetectorRef) {
    this.scheduleForm = this.fb.group({
      fertiliser: ['', Validators.required],
      quantity: [null, [Validators.required, Validators.min(0.1)]],
      unit: ['kg', Validators.required],
      days_after_sowing: [null, [Validators.required, Validators.min(0)]],
      farm_id: [null, Validators.required]
    });
  }

  submit(): void {
    if (this.scheduleForm.invalid) return;

    this.scheduleService.createSchedule(this.scheduleForm.value).subscribe({
      next: () => {
        this.success = true;
        this.scheduleForm.reset();
        this.cdr.detectChanges();
      },
      error: err => console.error('Failed to create schedule:', err)
    });
  }
}
