# import library socket karena akan menggunakan IPC socket
import socket
# definisikan alamat IP binding  yang akan digunaka
ip = '127.0.0.1'
# definisikan port number binding  yang akan digunakan
port = 12345
# definisikan ukuran buffer untuk mengirimkan pesan
BUFFER_SIZE = 1024
# buat socket bertipe TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# lakukan bind
s.bind((ip, port))
# server akan listen menunggu hingga ada koneksi dari client
s.listen(5)
# lakukan loop forever
while 5:
    # menerima koneksi
    conn, addr = s.accept()
    # menampilkan koneksi berupa IP dan port client yang terhubung menggunakan print
    pesan = "halo " + str(addr) + " Anda telah berhasil terkoneksi ke server"
    print(pesan)
    # menerima data berdasarkan ukuran buffer
    data = conn.recv(BUFFER_SIZE)
    # menampilkan pesan yang diterima oleh server menggunakan print
    print("Pesan diterima:", data.decode())
    # mengirim kembali data yang diterima dari client kepada client
    print('kirim pesan kepada client : ')
    received = input('')
    conn.send(received.encode())
    #tutup koneksi
    conn.close()
