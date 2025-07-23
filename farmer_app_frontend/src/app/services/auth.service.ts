import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, tap, switchMap } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
import { User } from '../models/models';
import { environment } from '../../environments/environment';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private apiBaseUrl = environment.apiBaseUrl;
  private userSubject = new BehaviorSubject<User | null>(null);
  private tokenSubject = new BehaviorSubject<string | null>(null);

  public user$ = this.userSubject.asObservable();
  public token$ = this.tokenSubject.asObservable();

  constructor(private http: HttpClient, private router: Router) {
    const token = this.getStoredToken();
    if (token) {
      this.tokenSubject.next(token);
      this.fetchUser(token).subscribe({
        next: user => this.setUser(user),
        error: () => this.clearUser()
      });
    }
  }

  private getStoredToken(): string | null {
    return localStorage.getItem('access_token');
  }

  private setToken(token: string): void {
    localStorage.setItem('access_token', token);
    this.tokenSubject.next(token);
  }

  private removeToken(): void {
    localStorage.removeItem('access_token');
    this.tokenSubject.next(null);
  }

  get user(): User | null {
    return this.userSubject.value;
  }

  setUser(user: User): void {
    this.userSubject.next(user);
  }

  clearUser(): void {
    this.userSubject.next(null);
  }

  getUserValue(): User | null {
    return this.userSubject.value;
  }

  isLoggedIn(): boolean {
  return !!localStorage.getItem('access_token');
}

  hasRole(role: string): boolean {
    return this.user?.roles?.includes(role) || false;
  }

  login(credentials: { user_name: string; password: string }): Observable<User> {
    return this.http.post<{ access_token: string }>(
      `${this.apiBaseUrl}/login`,
      credentials
    ).pipe(
      switchMap(response => {
        const token = response.access_token;
        this.setToken(token);
        return this.fetchUser(token);
      }),
      tap(user => {
        this.setUser(user);
        this.router.navigate(['/home']);
      })
    );
  }

  logout(): void {
    this.removeToken();
    this.clearUser();
    this.router.navigate(['/login']);
  }

  private fetchUser(token: string): Observable<User> {
    return this.http.get<User>(`${this.apiBaseUrl}/get-user`, {
      headers: new HttpHeaders({
        Authorization: `Bearer ${token}`
      })
    });
  }
}
