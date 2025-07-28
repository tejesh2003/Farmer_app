import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { ScheduleService } from '../../services/schedule.service';
import { Navbar } from '../navbar/navbar';

@Component({
  selector: 'app-create-schedule',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, Navbar],
  templateUrl: './create-schedule.html',
  styleUrls: ['./create-schedule.css']
})
export class CreateSchedule implements OnInit {
  scheduleForm: FormGroup;
  success = false;
  farmId!: number;

  fertilizers = [
    { name: 'Urea', unit: 'kg' },
    { name: 'DAP', unit: 'kg' },
    { name: 'MOP', unit: 'kg' },
    { name: 'Gypsum', unit: 'kg' },
    { name: 'Compost', unit: 'kg' },
    { name: 'Micronutrients', unit: 'kg' },
    { name: 'Liquid Fertilizer', unit: 'L' }
  ];

  constructor(
    private fb: FormBuilder,
    private route: ActivatedRoute,
    private scheduleService: ScheduleService,
    private cdr: ChangeDetectorRef
  ) {
    this.scheduleForm = this.fb.group({
      fertiliser: ['', Validators.required],
      quantity: [null, [Validators.required, Validators.min(1)]],
      unit: [{ value: '', disabled: true }, Validators.required],
      days_after_sowing: [null, [Validators.required, Validators.min(0)]]
    });
  }

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      const id = params.get('id');
      if (id) {
        this.farmId = +id;
      }
    });

    this.scheduleForm.get('fertiliser')?.valueChanges.subscribe(name => {
      const fert = this.fertilizers.find(f => f.name === name);
      if (fert) {
        this.scheduleForm.get('unit')?.setValue(fert.unit);
      } else {
        this.scheduleForm.get('unit')?.reset();
      }
    });
  }

  submit(): void {
    if (this.scheduleForm.invalid) return;

    const formValue = this.scheduleForm.getRawValue(); // to include disabled fields
    const payload = {
      ...formValue,
      farm_id: this.farmId
    };

    this.scheduleService.createSchedule(payload).subscribe({
      next: () => {
        this.success = true;
        this.scheduleForm.reset();
        this.cdr.detectChanges();
      },
      error: err => console.error('Failed to create schedule:', err)
    });
  }
}
