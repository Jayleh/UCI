Sub stockVolume():
    ' Loop thru each year of stock data and grab the total amount of volume each stock had over the year
    ' Also need to display the ticker symbol to coincide with the total volume
    
    ' Declare ticker letter
    Dim ticker As String
        
    ' Instantiate total volume
    Dim volume As Long
    volume = 0
    
    Dim summary_table_row As Integer
    summary_table_row = 2

    ' Get last row of worksheet
    Dim lr As Integer
    lr = ThisWorkbook.Sheets("A").Cells(Rows.Count, 1).End(xlUp).Row
    lr = rowCount - 1

    ' The for loop
    Dim i As Integer
    Dim j As Integer
    ticker = Cells(i, 1).Value
    
    For i = 2 To lr
        For j = 1 to lr
            If ticker <> Cells(i + 1, 1).Value Then
                Range("I" & summary_table_row).Value = ticker
                summary_table_row = summary_table_row + 1
                volume = volume + Cells(i, 7).Value
                Range("J" & summary_table_row).Value = volume
                volume = 0
            Else
                volume = volume + Cells(i, 7).Value            
        Next j
    Next i

End Sub