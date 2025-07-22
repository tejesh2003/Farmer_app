import { Component } from '@angular/core';
import { InputTextModule } from 'primeng/inputtext';
import { PasswordModule } from 'primeng/password';
import { ButtonModule } from 'primeng/button'
import { environment } from '../../environments/environment';
import { HttpClient } from '@angular/common/http';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';

const apiUrl=environment.apiBaseUrl;

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

  constructor(private http: HttpClient){}

  onSubmit(){
    const payload=this.form.value;

    this.http.post(apiUrl+'/login', payload)
    .subscribe({
      next : res => console.log('success',res),
      error: res=> console.log('error',res)
    })
  }
}
