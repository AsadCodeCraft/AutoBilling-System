# Auto Billing System Using Computer Vision

## Introduction

Auto Billing Desk Using Computer Vision is a project aimed at revolutionizing the retail checkout process through the integration of machine learning and computer vision technologies. By automating the product identification and checkout process, this project seeks to enhance efficiency, reduce human error, and improve the overall shopping experience for customers.

## Main Objective

The primary goal of this project is to develop a self-checkout system that leverages computer vision to detect and classify products in real-time. By deploying machine learning models on edge devices like Raspberry Pi, the project aims to enable seamless and efficient transactions without the need for manual intervention. The system should accurately identify products, provide real-time updates to the user interface, and facilitate smooth checkout experiences for customers.

## Project Details

### 1. Client Side
The client-side interface is responsible for providing a user-friendly experience for customers during the checkout process. Developed using HTML, CSS, JavaScript, and jQuery, the interface continuously listens to the REST API for updates on detected products. Upon receiving product information, it dynamically updates the cart page, allowing users to review and add items to their cart with ease.

### 2. RPI Server
The Raspberry Pi (RPI) server hosts the object detection and classification model, making it capable of processing images captured by a camera in real-time. Utilizing frameworks like TensorFlow or OpenCV, the RPI server identifies products within the camera's field of view. Once a product is successfully classified, the server communicates with the REST API, sending relevant product details such as ID, name, quantity, and price.

### 3. REST API
The REST API serves as the central communication hub between the RPI server and the client-side interface. Built using Node.js and Express.js, the API receives product information from the RPI server and forwards it to the client-side interface for display. Additionally, it handles requests from the client-side interface, such as adding products to the cart and updating inventory information. The API ensures seamless integration between the various components of the self-checkout system.

## Usage

To use the Auto Billing Desk system:

1. Ensure the RPI server is set up with the object detection and classification model.
2. Start the REST API server on the designated host.
3. Access the client-side interface from a web browser and initiate the checkout process.
4. As products are detected and classified by the RPI server, they will be displayed on the client-side interface.
5. Review the detected products and add them to the cart as needed.
6. Complete the checkout process, and the system will finalize the transaction, updating inventory records as necessary.

## Contribution

Contributions to the project are welcome! Whether it's adding new features, improving existing functionality, or fixing bugs, feel free to contribute by opening issues or submitting pull requests.
