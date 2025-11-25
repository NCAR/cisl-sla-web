# cisl-sla-web
A website that provides links to all the defined CISL Service Level Agreements (SLAs)

## Overview
This web application serves as a centralized hub for accessing Service Level Agreements (SLAs) for CISL services. It provides a clean, user-friendly interface to browse and access SLAs for various services including HPC systems, data platforms, and infrastructure services.

## Contributing

### Adding a New Service SLA

To add a new service to the SLA portal, follow these steps:

1. **Fork the repository**
   - Create a fork of this repository to your GitHub account

2. **Add your service to `slas.yaml`**
   - Open the `slas.yaml` file in the root directory
   - Add a new entry for your service following this format:
```yaml
   - service_name: Your Service Name
     service_logo: static/logos/YourService_Logo.png
     service_description: Brief description of your service
     service_sla_link: https://link-to-your-sla-documentation
```

3. **Add a logo**
   - Place your service logo in the `static/logos/` directory
   - Recommended format: PNG with transparent background
   - Recommended size: Square aspect ratio, at least 200x200px
   - File naming convention: `ServiceName_Logo.png`

4. **Test locally** (optional but recommended)
   - Install dependencies: `pip install -r requirements.txt`
   - Run the application: `flask run`
   - Verify your service appears correctly at `http://localhost:5000`

5. **Open a Pull Request**
   - Commit your changes with a clear message (e.g., "Add SLA for [Service Name]")
   - Push to your fork
   - Open a Pull Request against the main repository
   - Provide a brief description of the service being added

### Example Entry
```yaml
- service_name: Derecho
  service_logo: static/logos/Derecho_Logo.png
  service_description: High-performance computing system
  service_sla_link: https://ncar-hpc-docs.readthedocs.io/en/latest/...
```

## Questions?

If you have questions about contributing or need assistance, please contact the CISL SLA Working Group or open an issue in this repository.