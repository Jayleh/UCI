Sub stockTotal():
          
    For Each ws In Worksheets
        ' Label new column headers
        ws.Range("I1").Value = "Ticker"
        ws.Range("J1").Value = "Yearly Change"
        ws.Range("K1").Value = "Percent Change"
        ws.Range("L1").Value = "Total Stock Volume"
                
        ' Declare ticker letter
        Dim ticker As String
        
        ' Instantiate ticker total
        Dim ticker_total As Double
        ticker_total = 0
        
        ' Instantiate ticker open and close prices
        Dim open_price, close_price As Double
        open_price = 0
        close_price = 0
        
        ' Instantiate ticker count
        Dim ticker_count As Long
        ticker_count = 1
        
        ' Declare yearly and percent changes
        Dim year_change, percent_change As Double
            
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

                ' Increase open and close prices
                open_price = open_price + ws.Cells(i, 3).Value
                close_price = close_price + ws.Cells(i, 6).Value

                ' Calculate yearly difference
                year_change = (close_price - open_price) / ticker_count

                ' Print yearly change in summary table
                ws.Range("J" & summary_table_row).Value = year_change
                
                ' Calculate percent change
                percent_change = (year_change / (open_price / ticker_count))

                ' Print percent change in summary table
                ws.Range("K" & summary_table_row).Value = percent_change

                ' Increase ticker total
                ticker_total = ticker_total + ws.Cells(i, 7).Value

                ' Print ticker total in summary table
                ws.Range("L" & summary_table_row).Value = ticker_total

                ' Increment summary table row
                summary_table_row = summary_table_row + 1

                ' Reset totals
                open_price = 0
                close_price = 0
                ticker_count = 1
                ticker_total = 0
            Else
                ' Default as increase ticker total
                open_price = open_price + ws.Cells(i, 3).Value
                close_price = close_price + ws.Cells(i, 6).Value
                ticker_count = ticker_count + 1
                ticker_total = ticker_total + ws.Cells(i, 7).Value
            End If

        Next i

        ' Autofit columns
        ws.Columns("J").AutoFit
        ws.Columns("K").AutoFit
        ws.Columns("L").AutoFit
        
        ' Format column K to percentage
        ws.Columns("K").EntireColumn.NumberFormat = "0.00%"

    Next ws

End Sub
