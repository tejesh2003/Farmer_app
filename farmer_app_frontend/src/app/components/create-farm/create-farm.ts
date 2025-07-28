import { Component, ChangeDetectorRef, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { FarmService } from '../../services/farm.service';
import { Navbar } from '../navbar/navbar';

@Component({
  selector: 'app-create-farm',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, Navbar],
  templateUrl: './create-farm.html',
  styleUrls: ['./create-farm.css']
})
export class CreateFarm implements OnInit {
  farmForm: FormGroup;
  success = false;
  farmerId!: number;

  constructor(
    private fb: FormBuilder,
    private farmService: FarmService,
    private cdr: ChangeDetectorRef,
    private route: ActivatedRoute
  ) {
    this.farmForm = this.fb.group({
      village: ['', Validators.required],
      sowing_date: ['', Validators.required],
      area: [null, [Validators.required, Validators.min(0.1)]],
      crop: ['', Validators.required]
    });
  }

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      const id = params.get('id');
      if (id) {
        this.farmerId = +id;
      }
    });
  }

  submit(): void {
    if (this.farmForm.invalid) return;

    const payload = {
      ...this.farmForm.value,
      farmer_id: this.farmerId
    };

    this.farmService.createFarm(payload).subscribe({
      next: () => {
        this.success = true;
        this.farmForm.reset();
        this.cdr.detectChanges();
      },
      error: err => console.error('Failed to create farm:', err)
    });
  }
}
