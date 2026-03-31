A Python-based desktop chat application combining a TCP server/client architecture with a custom UDP peer-to-peer protocol for direct messaging and file transfers.
How it works:
The app runs on two layers. A central TCP server handles user authentication, online presence, group chat, and private messaging — acting as a coordination hub. When two users want to communicate directly, they negotiate a connection through the server and then switch to a dedicated UDP peer-to-peer channel for low-latency chat and file transfers, bypassing the server entirely.
The P2P layer implements a custom reliable messaging protocol over UDP — including sequence numbers, acknowledgements, and automatic retransmission — to guarantee delivery of both messages and files, which are transferred in chunks with full integrity tracking.
Features:

User registration & login (credential stored locally)
Group chat and private messaging via TCP
Direct P2P chat sessions over UDP with reliable delivery
File transfer over the P2P channel (images, documents, any file type)
Public/private visibility toggle
Tkinter GUI with tabbed interface for group, private, and P2P chat
Built-in server manager — host and monitor a server from within the app
