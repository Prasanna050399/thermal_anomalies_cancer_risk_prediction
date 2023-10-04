# Breast Cancer Early Detection System

## Overview

The Breast Cancer Early Detection System is a comprehensive solution designed to aid in the early detection of breast cancer using thermal images. The system consists of four main modules:

1. **Pre-Processing**: This module is responsible for extracting the Region of Interest (ROI) from thermal images, preparing them for further analysis.

2. **Anomaly Detection**: After extracting the ROI, this module identifies and highlights thermal anomalies present within the images.

3. **Neural Network Classifier**: The Neural Network Classifier takes the processed thermal images and classifies them as either positive or negative for breast masses. It employs a backpropagation neural network for this task.

4. **Graphical User Interface (GUI)**: The GUI module provides an intuitive interface for users to interact with the system, making it user-friendly and accessible within the organization.

## Tools and Technologies Used

The development of this system utilizes the following tools and technologies:

- **Python**: The primary programming language for building and implementing the modules.

- **OpenCV**: Used for image processing and manipulation, particularly in the Pre-Processing and Anomaly Detection modules.

- **TensorFlow**: Utilized for implementing and training the neural network in the Neural Network Classifier module.

- **PyQt5**: Employed to create the Graphical User Interface (GUI) for user interaction.

- **Reportlab**: Used for generating reports and visualizations of the system's results.

- **Scikit-image**: Provides additional image processing capabilities.

- **NumPy**: Used for numerical and array operations.

- **MongoDB**: May be used for data storage and retrieval, although further details are needed.

## Conclusion

The Breast Cancer Early Detection System offers a promising approach to the early detection of breast cancer using thermal images. By detecting thermal anomalies and employing a neural network-based classifier, the system aims to provide accurate results.

The system has displayed an impressive accuracy rate of 95.45% on testing data, indicating its potential as a valuable tool in the field of cancer research. While these results are promising, there is still room for improvement, and ongoing development may lead to even better outcomes. The system's ability to potentially make breakthroughs in cancer research is a testament to its significance and impact.

For more details on installation, usage, and contributions, please refer to the relevant sections in this repository.

For more information about the project, please refer to the project [report]().
