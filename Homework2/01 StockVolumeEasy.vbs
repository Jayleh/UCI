Sub stockTotal():
          
    For Each ws In Worksheets
        ' Label new column headers and autofit
        ws.Range("I1").Value = "Ticker"
        ws.Range("J1").Value = "Total Stock Volume"
        ws.Columns("J").AutoFit
        
        ' Declare ticker letter
        Dim ticker As String
        
        ' Instantiate ticker total
        Dim ticker_total As Double
        ticker_total = 0
    
        ' Keep track of location of each ticker for summary table
        Dim summary_table_row As Long
        summary_table_row = 2

        ' For the loop
        Dim i, lr As Long
        lr = ws.Cells(Rows.Count, 1).End(xlUp).Row

        ' Loop through all tickers
        For i = 2 To lr

            If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
                ' Set ticker letter
                ticker = ws.Cells(i, 1).Value

                ' Print ticker in summary table
                ws.Range("I" & summary_table_row).Value = ticker

                ' Increase ticker total
                ticker_total = ticker_total + ws.Cells(i, 7).Value

                ' print ticker total in summary table
                ws.Range("J" & summary_table_row).Value = ticker_total

                ' Increment summary table row
                summary_table_row = summary_table_row + 1

                ' Reset ticker total
                ticker_total = 0
            Else
                ' Default as increase ticker total
                ticker_total = ticker_total + ws.Cells(i, 7).Value
            End If

        Next i
    
    Next ws

End Sub
