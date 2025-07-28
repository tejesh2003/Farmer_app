import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-all-users',
  templateUrl: './all-users.html',
  styleUrls: [],
  imports: [CommonModule]
})
export class AllUsers implements OnInit {
  users: any[] = [];

  constructor(private userService: UserService, private cdr : ChangeDetectorRef) {}

  ngOnInit() {
    this.userService.getAllUsers().subscribe({
      next: (data) => {
        this.users = data
        this.cdr.detectChanges();
      },
      error: (err) => console.error('Error fetching users', err)
    });
  }
}
