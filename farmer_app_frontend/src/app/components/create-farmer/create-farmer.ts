import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { FarmerService } from '../../services/farmer.service';
import { CountryService } from '../../services/country.service';

@Component({
  selector: 'app-create-farmer',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './create-farmer.html',
  styleUrl: './create-farmer.css'
})
export class CreateFarmer implements OnInit {
  farmerForm: FormGroup;
  success = false;
  countries: { id: number; country_name: string }[] = [];

  constructor(
    private fb: FormBuilder,
    private farmerService: FarmerService,
    private countryService: CountryService,
    private cdr: ChangeDetectorRef
  ) {
    this.farmerForm = this.fb.group({
      name: ['', Validators.required],
      phone: ['', [Validators.required, Validators.pattern(/^\d{10}$/)]],
      language: ['', Validators.required],
      country: ['', Validators.required]
    });
  }

  ngOnInit(): void {
    this.countryService.getAllCountries().subscribe({
      next: (res) => {
        this.countries = res;
        this.cdr.detectChanges();
      },
      error: (err) => console.error('Failed to fetch countries:', err)
    });
  }

  submit(): void {
    console.log("Submit clicked");
    if (this.farmerForm.invalid) return;

    this.farmerService.createFarmer(this.farmerForm.value).subscribe({
      next: () => {
        this.success = true;
        this.cdr.detectChanges();
        this.farmerForm.reset();
      },
      error: (err) => console.error('Failed to create farmer:', err)
    });
  }
}
