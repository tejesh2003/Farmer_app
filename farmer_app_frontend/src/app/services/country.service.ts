import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CountryService {
  private baseUrl = `${environment.apiBaseUrl}/country`;

  constructor(private http: HttpClient) {}

  createCountry(name: string): Observable<any> {
    return this.http.post<any>(this.baseUrl, { name }); 
  }


  getAllCountries(): Observable<{ id: number; country_name: string }[]> {
    const url = `${environment.apiBaseUrl}/all-countries`;
    return this.http.get<{ id: number; country_name: string }[]>(url);
  }
}
