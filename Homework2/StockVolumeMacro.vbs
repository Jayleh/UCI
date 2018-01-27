Sub stockVolume():
    ' Loop thru each year of stock data and grab the total amount of volume each stock had over the year
    ' Also need to display the ticker symbol to coincide with the total volume
    
    ' declare variables
    Dim ticker As String
    Dim volume As Long
    
    ' get length of worksheet
    Dim rowCount As Integer
    rowCount = ThisWorkbook.Sheets("A").Cells(Rows.Count, 1).End(xlUp).Row
    rowCount = rowCount - 1

    ' the for loop
    Dim i As Integer
    Dim j As Integer
    ticker = Cells(i + 1, j).Value
    volume = 0

    For i = 1 To rowCount
        For j = 1 to rowCount
            If ticker <> Cells(i - 1, 1).Value Then
                
            
        Next j
    Next i

End Sub