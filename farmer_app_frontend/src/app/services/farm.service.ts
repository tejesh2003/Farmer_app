import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import { CreateFarm } from '../components/create-farm/create-farm';

@Injectable({
  providedIn: 'root'
})
export class FarmService {
  private baseUrl = `${environment.apiBaseUrl}/farm`;

  constructor(private http: HttpClient) {}

  createFarm(farm: CreateFarm): Observable<any> {
    return this.http.post<any>(this.baseUrl, farm);
  }
}
