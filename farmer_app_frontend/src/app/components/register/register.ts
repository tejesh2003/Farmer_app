import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { InputTextModule } from 'primeng/inputtext';
import { PasswordModule } from 'primeng/password';
import { ButtonModule } from 'primeng/button';
import { environment } from '../../../environments/environment';

const apiUrl = environment.apiBaseUrl;

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [ReactiveFormsModule,  InputTextModule, PasswordModule, ButtonModule],
  templateUrl: './register.html',
  styleUrl: './register.css'
})
export class Register {
  form= new FormGroup({
    user_name : new FormControl(''),
    password : new FormControl('')
  });

  constructor(private http:HttpClient) {}

  onSubmit(){
    const payload = this.form.value;

    this.http.post(apiUrl+'/register',payload)
    .subscribe({
      next : res => console.log('success',res),
      error : res => console.log('error',res)
    })
  }
}
