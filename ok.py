<?php 
// koneksi ke database
$conn = mysqli_connect("localhost","root","","tugasakhir");

function tambah ($data) {
	global $conn;
	$status = htmlspecialchars($data["status"]);
	$nama = htmlspecialchars($data["nama"]);
	$urut = htmlspecialchars($data["urut"]);
	$situs = htmlspecialchars($data["situs"]);
	$alumni = htmlspecialchars($data["alumni"]);

	// masukin data ke dalam database tabel stand
	$sql = "INSERT INTO stand VALUES ('', '$nama', '$status', '$urut', '$alumni', '$situs')";
	$mam = mysqli_query($conn,$sql);
	return mysqli_affected_rows($conn);

}

function upload(){
	$nama = $_FILES['gambar']['name'];
	$ukuran = $_FILES['gambar']['size'];
	$error = $_FILES['gambar']['error'];
	$tempat = $_FILES['gambar']['tmp_name'];

	// cek gambar diupload apa tidak
	if ($error === 4){ //4 => tidak ada gambar yang diupload
		echo "<script>
				alert('Pilih Gambar Terlebih Dahulu')
				</script>";
		return false;
	}

	// cek yang di upload adalah gambar dengan format ditentukan
	$formatvalid = ['jpg', 'jpeg', 'png'];
	$format = explode('.', $nama);
	$format = strtolower(end($format));
	if ( !in_array($format, $formatvalid) ){
		echo "<script>
				alert('yang anda upload bukan gambar')
				</script>";
		return false;
	}

	//  cek ukuran max gambar
	if ($ukuran > 9000000000){
		echo "<script>
				alert('ukuran gambar terlalu besar')
				</script>";
		return false;
	}
	// rename
	$newnama = uniqid();
	$newnama .= '.';
	$newnama .= $format;
	// moving file setelah pengecekan
	$qwe = move_uploaded_file($tempat, 'img/' . $newnama);
	return $newnama;
}

function query($tag){
	global $conn;
	$result = mysqli_query($conn, $tag);
	$rows = [];
	while ($row = mysqli_fetch_assoc($result)) {
		$rows[] = $row;
	}
	return $rows;
}

function cari($keyword){
	$query = "SELECT * FROM stand WHERE nama LIKE '%$keyword%' OR status LIKE '%$keyword%' OR urut LIKE '%$keyword%'";
	return query($query);
}

function hapus($id){
	global $conn;
	mysqli_query($conn,"DELETE FROM stand where id = $id");
	return mysqli_affected_rows($conn);
}
function ubah($data){
	global $conn;
	$id = $data["id"];
	$status = htmlspecialchars($data["status"]);
	$nama = htmlspecialchars($data["nama"]);
	$urut = htmlspecialchars($data["urut"]);
	$situs = htmlspecialchars($data["situs"]);
	$alumni = htmlspecialchars($data["alumni"]);
	$sql = "UPDATE stand SET nama = '$nama', status = '$status', urut = '$urut', alumni = '$alumni', situs = '$situs' where id = $id";
	mysqli_query($conn,$sql);
	return mysqli_affected_rows($conn);
}

function daftar($data){
	global $conn;
	$kampus = htmlspecialchars($data["kampus"]);
	$nama = htmlspecialchars($data["nama"]);
	$email = htmlspecialchars($data["email"]);
	$alumni = htmlspecialchars($data["alumni"]);
	$keterangan = htmlspecialchars($data["keterangan"]);
	$kategori = htmlspecialchars($data["kategori"]);

	$gambar = upload();
	if (!$gambar){
		return false;
	}

	$sql = "INSERT INTO daftar VALUES ('', '$nama',  '$kampus', '$email', '$kategori', '$alumni', '$gambar', '$keterangan')";
	mysqli_query($conn,$sql);
	return mysqli_affected_rows($conn);
}
?>
