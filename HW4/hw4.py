from flask import Flask, request
from formatter import format_records
from database_handler import execute_query

app = Flask(__name__)

@app.route("/order_price")
def order_price(country=None):
    country = request.args.get('country', default=None, type=str)
    if country:
        query = """
        SELECT invoices.BillingCountry, SUM(invoice_items.UnitPrice) AS TotalSales
        FROM invoices
        JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
        WHERE invoices.BillingCountry = ?
        GROUP BY invoices.BillingCountry 
        ORDER BY TotalSales DESC
        """
        result = execute_query(query=query, args=(country,))
    else:
        query = """
        SELECT invoices.BillingCountry, SUM(invoice_items.UnitPrice) AS TotalSales
        FROM invoices
        JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
        GROUP BY invoices.BillingCountry 
        ORDER BY TotalSales DESC
        """
        result = execute_query(query=query)
    return format_records(result)

@app.route("/get_all_info_about_track")
def get_all_info_about_track(tracked=None):
    tracked = request.args.get('tracked', default=None, type=int)
    if tracked:
        query = """
        SELECT tracks.Name, albums.Title AS AlbumName, artists.Name AS ArtistName,
        GROUP_CONCAT(playlists.Name) AS Playlists, invoice_items.UnitPrice
        FROM tracks
        JOIN albums ON tracks.AlbumId = albums.AlbumId
        JOIN artists ON albums.ArtistId = artists.ArtistId
        JOIN playlist_track ON tracks.TrackId = playlist_track.TrackId
        JOIN playlists ON playlist_track.PlaylistId = playlists.PlaylistId
        JOIN invoice_items ON tracks.TrackId = invoice_items.TrackId
        WHERE tracks.TrackId = ?
        GROUP BY tracks.TrackId, albums.Title, artists.Name, invoice_items.UnitPrice
        """
        result = execute_query(query=query, args=(tracked,))
    else:
        query = """
        SELECT tracks.Name, albums.Title AS AlbumName, artists.Name AS ArtistName,
        GROUP_CONCAT(playlists.Name) AS Playlists, invoice_items.UnitPrice
        FROM tracks
        JOIN albums ON tracks.AlbumId = albums.AlbumId
        JOIN artists ON albums.ArtistId = artists.ArtistId
        JOIN playlist_track ON tracks.TrackId = playlist_track.TrackId
        JOIN playlists ON playlist_track.PlaylistId = playlists.PlaylistId
        JOIN invoice_items ON tracks.TrackId = invoice_items.TrackId
        GROUP BY tracks.TrackId, albums.Title, artists.Name, invoice_items.UnitPrice
                """
        result = execute_query(query=query)
    return format_records(result)

# i didn’t quite understand task 3*, but I hope it’s correct
@app.route("/album_listening_time")
def album_listening_time():
    query = """
    SELECT albums.Title AS AlbumName, SUM(tracks.Milliseconds) / 60000 AS TotalListeningTimeInMinutes
    FROM tracks
    JOIN albums ON tracks.AlbumId = albums.AlbumId
    GROUP BY albums.Title
    ORDER BY TotalListeningTimeInMinutes DESC   
    """
    result = execute_query(query=query)
    return format_records(result)

@app.route("/stats_by_city")
def stats_by_city():
    genre = request.args.get('genre', type=str)
    if not genre:
        return "Please indicate genre!"
    query = """
    WITH RankedCities AS (
        SELECT BillingCity,
        RANK() OVER (ORDER BY COUNT(*) DESC) as rank
        FROM invoices
        JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
        JOIN tracks ON invoice_items.TrackId = tracks.TrackId
        JOIN genres ON tracks.GenreId = genres.GenreId
        WHERE genres.Name = ?
        GROUP BY BillingCity
    )
    SELECT BillingCity
    FROM RankedCities
    WHERE rank = 1
    """
    result = execute_query(query=query, args=(genre,))
    return format_records(result)