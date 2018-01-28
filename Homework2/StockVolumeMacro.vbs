Sub stockVolume():
    ' Loop thru each year of stock data and grab the ticker amount of volume each stock had over the year
    ' Also need to display the ticker symbol to coincide with the ticker volume
    
    ' Declare ticker letter
    Dim ticker As String
        
    ' Instantiate ticker volume
    Dim ticker_volume As Long
    ticker_volume = 0
    
    ' Keep track of location of each ticker for summary table
    Dim summary_table_row As Integer
    summary_table_row = 2

    ' Get last row of worksheet
    Dim lr As Integer
    lr = ThisWorkbook.Sheets("A").Cells(Rows.Count, 1).End(xlUp).Row

    ' Loop through all tickers
    Dim i As Integer
    
    For i = 2 To lr
        
        If Cells(i + 1, 1) <> Cells(i, 1).Value Then
            ' Set ticker ticker letter
            ticker = Cells(i, 1).Value
            
            ' Print ticker in summary table
            Range("I" & summary_table_row).Value = ticker            

            ' Increase ticker volume
            ticker_volume = volume + Cells(i, 7).Value

            ' print ticker volume in summary table
            Range("J" & summary_table_row).Value = ticker_volume

            ' Increment summary table row
            summary_table_row = summary_table_row + 1

            ' Reset ticker volume
            ticker_volume = 0
        Else
            ' Default as increase ticker volume
            ticker_volume = ticker_volume + Cells(i, 7).Value
        End If         
        
    Next i

End Sub