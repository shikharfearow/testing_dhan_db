def generate_html(stock_data):
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="refresh" content="1">
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333;
                padding: 20px;
            }
            h1 {
                color: #444;
            }
            .stock-list {
                list-style-type: none;
                padding: 0;
            }
            .stock-list li {
                background-color: #fff;
                margin-bottom: 10px;
                padding: 15px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
            .stock-list li .symbol {
                font-weight: bold;
                font-size: 1.2em;
            }
            .stock-list li .price {
                color: #28a745;
                font-size: 1.1em;
            }
            .stock-list li .change {
                color: #dc3545;
                font-size: 1.1em;
            }
        </style>
        <title>Stock List</title>
    </head>
    <body>
        <h1>Stock Prices</h1>
        <ul class="stock-list">
    '''
    
    change_class = 'change'
    html_content += f'''
                <span class="symbol">{stock_data['Security_ID']}</span><br>
                <span class="price">VOLUME: ${stock_data['Volume']}</span><br>
                <span class="price">LTP: ${stock_data['LTP']}</span><br>
                <span class="{change_class}">Change: {stock_data['VolumeChange']}</span>
        '''
    
    html_content += '''
        </ul>
    </body>
    </html>
    '''
    return html_content