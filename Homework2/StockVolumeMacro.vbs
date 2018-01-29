Sub stocktotal():
    ' Loop thru each year of stock data and grab the ticker amount of volume each stock had over the year
    ' Also need to display the ticker symbol to coincide with the ticker volume
    
    ' Declare ticker letter
    Dim ticker As String
        
    ' Instantiate ticker total
    Dim ticker_total As Long
    ticker_total = 0
    
    ' Keep track of location of each ticker for summary table
    Dim summary_table_row As Integer
    summary_table_row = 2

    ' Get last row of worksheet
    Dim lr As Long
    lr = ThisWorkbook.Sheets("A").Cells(Rows.Count, 1).End(xlUp).Row

    ' Loop through all tickers
    Dim i As Long
    
    For i = 2 To lr
        
        If Cells(i + 1, 1) <> Cells(i, 1).Value Then
            ' Set ticker ticker letter
            ticker = Cells(i, 1).Value
            
            ' Print ticker in summary table
            Range("I" & summary_table_row).Value = ticker            

            ' Increase ticker total
            ticker_total = ticker_total + Cells(i, 7).Value

            ' print ticker total in summary table
            Range("J" & summary_table_row).Value = ticker_total

            ' Increment summary table row
            summary_table_row = summary_table_row + 1

            ' Reset ticker total
            ticker_total = 0
        Else
            ' Default as increase ticker total
            ticker_total = ticker_total + Cells(i, 7).Value
        End If         
        
    Next i

End Sub