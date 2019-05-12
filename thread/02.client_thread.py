# import socket dan sys
import socket, sys
# fungsi utama
import uuid
print("Nama : Nero Chaniago")  # Ganti Nama_Mahasiswa dengan nama Anda
print("NIM : 1301164305")	# Ganti NIM_Mahasiswa dengan NIM Anda
print("MAC Address Komputer / Laptop : ", hex(uuid.getnode()))
print('')

def main():
    # buat socket bertipe TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # tentukan IP server target
    ip = "172.89.2.153"
    
    # tentukan port server
    port = 12345

    # lakukan koneksi ke server
    try:
        sock.connect((ip, port))
    except:
        # print error
        print("Koneksi error")
        # exit
        sys.exit()
    
    # tampilkan menu, enter quit to exit
    print("Masukkan 'quit' untuk keluar")
    message = input(" -> ")

 # selama pesan bukan "quit", lakukan loop forever
    while message != 'quit':
        # kirimkan pesan yang ditulis ke server
        sock.send(message.encode())
        
        # menu (user interface)
        message = input(" -> ")

    # send "quit" ke server
    sock.send(b'--quit--')

# panggil fungsi utama
if __name__ == "__main__":
    main()