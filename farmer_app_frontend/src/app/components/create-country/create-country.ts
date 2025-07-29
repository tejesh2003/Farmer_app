import { ChangeDetectorRef, Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { CountryService } from '../../services/country.service';

@Component({
  selector: 'app-create-country',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './create-country.html',
  styleUrl: './create-country.css'
})
export class CreateCountry {
  countryForm: FormGroup;
  success = false;

  constructor(private fb: FormBuilder, private countryService: CountryService, private cdr: ChangeDetectorRef) {
    this.countryForm = this.fb.group({
      country: ['', Validators.required]
    });
  }

  submit(): void {
    if (this.countryForm.invalid) return;

    this.countryService.createCountry(this.countryForm.value).subscribe({
      next: () => {
        this.success = true;
        this.cdr.detectChanges();
        this.countryForm.reset();
      },
      error: (err) => console.error('Failed to create country:', err)
    });
  }
}
