import { HttpInterceptorFn } from '@angular/common/http';
import { environment } from '../../environments/environment';

export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const isBackend = req.url.startsWith(environment.apiBaseUrl);
  const token = localStorage.getItem('access_token');

  if (isBackend && token) {
    const modifiedReq = req.clone({
      headers: req.headers.set('Authorization', `Bearer ${token}`)
    });
    return next(modifiedReq);
  }

  return next(req);
};
