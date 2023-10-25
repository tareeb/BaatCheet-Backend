# BaatCheet-Backend
An End to End Encrypted Chat Application

## Tech Stack : 
- Django for Backend
- React for Frontend 
- SQL for Data Storage

### Front End Repo : 
You can find the Front End project repository [here](https://github.com/tareeb/baatcheet-Frontend).

## Technical Documentation : 

- ## Real Time Communication :
  We have incorporated Django Channels, a powerful library built on top of websockets, to handle real-time messaging functionality. Django Channels allow users to communicate through channel layers, enabling seamless and efficient communication between users.
  
- ## End to End Encryption :
  - ### Package:
      We are using WEB CRYPTO API for encryption and decryption of texts. Web crypto Api provides low level interface for dealing          with cryptographic keys. The Web Crypto API supports a variety of cryptographic algorithms, including symmetric ciphers              (e.g., AES), asymmetric ciphers (e.g., RSA), hash functions (e.g., SHA-256), and digital signature algorithms (e.g., ECDSA). 
      These algorithms enable developers to secure data transmission, store sensitive information securely, and implement various 
      cryptographic protocols.
  
   - ### Algorithms:
       We are using both symmetric and asymmetric approach for our application.
       We are using asymmetric ECHC for agreeing upon same secret key and then we are using AES-256 bit for encryption and 
       decryption of texts

   - ### ECDH:
       In our application we are using elliptic curve Diffie-Hellman (ECDH) for generation of public private key pair generation. It 
       is widely used for key exchange so that two users can agree upon same secret key. We are using P-256 curve for generation of 
       key pair. It is used as a standard.

   - ### Symmetric key generation:
        After generating public and private key we are then deriving AES-256 bit key that will be used for encryption and decryption         of messages. We are using 256 AES algorithm in GCM mode for encryption and decryption and with each message we are also              sending random IV to increase the security of the system

## Problem and Further Goals:
  This End-to-End Chat Application stores encryption keys on the client side, rather than on the server side. Consequently, if a user loses their encryption key, there is no method to recover encrypted messages from the server, as the necessary decryption key is unavailable. It is imperative to establish a secure key management system that allows for key storage and retrieval to enhance the application's functionality.
  

### Screenshots : 
![logo4](https://github.com/tareeb/BaatCheet-Backend/assets/67794123/e29ec383-08aa-4f1c-b7df-3311970f8259)

![img2](https://github.com/tareeb/BaatCheet-Backend/assets/67794123/705b87f8-64ea-4538-aa4b-6f662de0525c)

![img3](https://github.com/tareeb/BaatCheet-Backend/assets/67794123/aca75fd1-3894-4124-aede-a1e98911cff9)

![img4](https://github.com/tareeb/BaatCheet-Backend/assets/67794123/28990fe7-9f92-476b-b356-61e2fa722c1b)

![img1](https://github.com/tareeb/BaatCheet-Backend/assets/67794123/be156e39-4236-40aa-b001-24330d413354)



