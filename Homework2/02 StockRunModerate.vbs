Sub stockRun():
    
    Dim ws As Worksheet

    For Each ws In Worksheets
        ' Label new column headers
        ws.Range("I1").Value = "Ticker"
        ws.Range("J1").Value = "Yearly Change"
        ws.Range("K1").Value = "Percent Change"
        ws.Range("L1").Value = "Total Stock Volume"
                
        ' Declare ticker letter
        Dim ticker As String
        
        ' Instantiate stock volume total
        Dim stock_volume As Double
        stock_volume = 0
        
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
                stock_volume = stock_volume + ws.Cells(i, 7).Value

                ' Print ticker total in summary table
                ws.Range("L" & summary_table_row).Value = stock_volume

                ' Increment summary table row
                summary_table_row = summary_table_row + 1

                ' Reset totals
                stock_volume = 0
            Else
                ' Default as increase ticker total
                stock_volume = stock_volume + ws.Cells(i, 7).Value
            End If

        Next i

        ' Autofit columns
        ws.Columns("J").AutoFit
        ws.Columns("K").AutoFit
        ws.Columns("L").AutoFit
        
        ' Format column K to percentage
        ws.Columns("K").EntireColumn.NumberFormat = "0.00%"

        ' Conditionaly format yearly change
        Dim k, summary_table_lr as Long
        summary_table_lr = ws.Cells(Rows.Count, 1).End(xlUp).Row

        For k = 2 To summary_table_lr

            If ws.Range("J" & k).Value > 0 Then
                ws.Range("J" & k).Interior.ColorIndex = 10            
            Else
                ws.Range("J" & k).Interior.ColorIndex = 9
            End If

        Next k

    Next ws

End Sub
