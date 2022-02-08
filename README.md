## Getting Started with VS Code

### Run the app locally with the Cloud Run Emulator

1. Click on the Cloud Code status bar and select 'Run on Cloud Run Emulator'.  
   ![image](./img/status-bar.png)

2. Use the Cloud Run Emulator dialog to specify your [builder option](https://cloud.google.com/code/docs/vscode/deploying-a-cloud-run-app#deploying_a_cloud_run_service). Cloud Code supports Docker, Jib, and Buildpacks. See the skaffold documentation on [builders](https://skaffold.dev/docs/pipeline-stages/builders/) for more information about build artifact types.  
   ![image](./img/build-config.png)

3. Click ‘Run’. Cloud Code begins building your image.

4. View the build progress in the OUTPUT window. Once the build has finished, click on the URL in the OUTPUT window to view your live application.  
   ![image](./img/cloud-run-url.png)

5. To stop the application, click the stop icon on the Debug Toolbar.

---
