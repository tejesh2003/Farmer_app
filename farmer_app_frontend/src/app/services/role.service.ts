import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import { EditRole } from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class RoleService {
  private addUrl = `${environment.apiBaseUrl}/add-role`;
  private removeUrl = `${environment.apiBaseUrl}/remove-role`;

  constructor(private http: HttpClient) {}

  addRole(payload: EditRole): Observable<any> {
    return this.http.post<any>(this.addUrl, payload);
  }

  removeRole(payload: EditRole): Observable<any> {
    return this.http.post<any>(this.removeUrl, payload);
  }
}
