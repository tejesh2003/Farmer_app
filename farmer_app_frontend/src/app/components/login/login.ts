import { Component } from '@angular/core';
import { InputTextModule } from 'primeng/inputtext';
import { PasswordModule } from 'primeng/password';
import { ButtonModule } from 'primeng/button'
import { AuthService } from '../../services/auth.service';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';


@Component({
  selector: 'app-login',
  standalone: true,
  imports: [ReactiveFormsModule,  InputTextModule, PasswordModule, ButtonModule],
  templateUrl: './login.html',
  styleUrl: './login.css'
})
export class Login {
  form= new FormGroup({
    user_name: new FormControl(''),
    password: new FormControl('')
  });

  constructor(private authService: AuthService) {}

  onSubmit() {
    if (this.form.invalid) return;
    const payload = {
      user_name: this.form.value.user_name ?? '',
      password: this.form.value.password ?? ''
    };


    this.authService.login(payload).subscribe({
      next: user => {
        console.log('Logged in as:', user);
      },
      error: err => {
        console.log('Login failed:', err);
      }
    });
  }
}
