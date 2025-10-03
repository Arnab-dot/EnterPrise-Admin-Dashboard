# Admin Dashboard SaaS – Finance & Client Management
## Overview
This project is a **robust, enterprise-grade Admin Dashboard** designed as a SaaS solution for **Finance and Client Management**. It allows organizations to manage clients, invoices, and users with **secure authentication and role-based access control**. Built to be scalable, modular, and professional, it’s suitable for small-to-medium businesses.

---

## Key Features

### User & Authentication
- **Custom User Model** with roles: `Admin`, `Staff`, `Viewer`
- JWT-based authentication with **access & refresh tokens**
- Role-based permissions: `Admin`, `Staff`, `SameOrganization`

### Organization Management
- Users are tied to an organization
- Admins can register users under their organization
- Ensures **data isolation between organizations**

### Client Management
- CRUD operations for clients
- Search, filter, and ordering support
- Role-based access control for actions

### Invoice Management
- CRUD operations for invoices
- Each invoice linked to a client & organization
- Filter, search, and order invoices by status, client, date, and amount
- Automatic user & organization association

### Security & Permissions
- JWT tokens with configurable lifetime
- Refresh tokens for session continuity
- Only authorized users from the same organization can access data
  
  ## Tech Stack
- **Backend:** Django 5.2, Django REST Framework  
- **Database:** PostgreSQL / SQLite  
- **Authentication:** JWT (access + refresh tokens) via DRF Simple JWT  
- **Frontend (planned):** ReactJS / Streamlit  

---
