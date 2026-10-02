# Inventaris 100 warning yang tersedia

Dihasilkan dari log compile baseline. Setiap pasangan sudah diperiksa nomor baris, kode, dan pesan setelah normalisasi nama variabel. Kolom berbeda akibat rename. Bukan daftar lengkap 264 warning.

| No. | Baris | Kolom Gold / Loco | Kode | Pesan Loco | Source Loco |
| ---: | ---: | --- | ---: | --- | --- |
| 1 | 922 | 15 / 18 | 43 | possible loss of data due to type conversion | `LR_SymbolDigits = MarketInfo(LR_CurrentSymbol,MODE_DIGITS) ;` |
| 2 | 931 | 16 / 25 | 43 | possible loss of data due to type conversion | `LR_Global251_Double_do = TimeCurrent() ;` |
| 3 | 994 | 15 / 24 | 43 | possible loss of data due to type conversion | `LR_Global036_Int_in = LR_FreezeLevelPriceDistance / LR_NormalizedPriceUnit ;` |
| 4 | 1069 | 16 / 22 | 43 | possible loss of data due to type conversion | `LR_Global304_Int_in = LR_Global125_Double_do * 60.0 ;` |
| 5 | 1155 | 15 / 18 | 43 | possible loss of data due to type conversion | `LR_SymbolDigits = MarketInfo(LR_CurrentSymbol,MODE_DIGITS) ;` |
| 6 | 1159 | 7 / 7 | 60 | possible use of uninitialized variable 'LR_Temp001_Bool_bo' | `if ( LR_Temp001_Bool_bo == true )` |
| 7 | 1868 | 15 / 18 | 43 | possible loss of data due to type conversion | `LR_SymbolDigits = MarketInfo(LR_CurrentSymbol,MODE_DIGITS) ;` |
| 8 | 2149 | 8 / 8 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 9 | 2157 | 10 / 10 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 10 | 2165 | 8 / 8 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 11 | 2173 | 10 / 10 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 12 | 2183 | 10 / 10 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 13 | 2194 | 10 / 10 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 14 | 2204 | 10 / 10 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 15 | 2215 | 10 / 10 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 16 | 2251 | 12 / 12 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 17 | 2259 | 14 / 14 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 18 | 2267 | 12 / 12 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 19 | 2275 | 14 / 14 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 20 | 2285 | 14 / 14 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 21 | 2296 | 14 / 14 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 22 | 2306 | 14 / 14 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 23 | 2317 | 14 / 14 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 24 | 2402 | 14 / 14 | 83 | return value of 'OrderClose' should be checked | `OrderClose(OrderTicket(),OrderLots(),MarketInfo(LR_CurrentSymbol,MODE_BID),99999,Red);` |
| 25 | 2405 | 12 / 12 | 83 | return value of 'OrderClose' should be checked | `OrderClose(OrderTicket(),OrderLots(),MarketInfo(LR_CurrentSymbol,MODE_ASK),99999,Red);` |
| 26 | 2434 | 14 / 14 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 27 | 2442 | 16 / 16 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 28 | 2450 | 14 / 14 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 29 | 2458 | 16 / 16 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 30 | 2468 | 16 / 16 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 31 | 2479 | 16 / 16 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 32 | 2489 | 16 / 16 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 33 | 2500 | 16 / 16 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 34 | 2585 | 16 / 16 | 83 | return value of 'OrderClose' should be checked | `OrderClose(OrderTicket(),OrderLots(),MarketInfo(LR_CurrentSymbol,MODE_BID),99999,Red);` |
| 35 | 2588 | 14 / 14 | 83 | return value of 'OrderClose' should be checked | `OrderClose(OrderTicket(),OrderLots(),MarketInfo(LR_CurrentSymbol,MODE_ASK),99999,Red);` |
| 36 | 2691 | 82 / 85 | 43 | possible loss of data due to type conversion | `OrderClose(OrderTicket(),OrderLots(),MarketInfo(LR_CurrentSymbol,MODE_BID),LR_Global038_Double_do,Red);` |
| 37 | 2691 | 10 / 10 | 83 | return value of 'OrderClose' should be checked | `OrderClose(OrderTicket(),OrderLots(),MarketInfo(LR_CurrentSymbol,MODE_BID),LR_Global038_Double_do,Red);` |
| 38 | 2695 | 82 / 85 | 43 | possible loss of data due to type conversion | `OrderClose(OrderTicket(),OrderLots(),MarketInfo(LR_CurrentSymbol,MODE_ASK),LR_Global038_Double_do,Red);` |
| 39 | 2695 | 10 / 10 | 83 | return value of 'OrderClose' should be checked | `OrderClose(OrderTicket(),OrderLots(),MarketInfo(LR_CurrentSymbol,MODE_ASK),LR_Global038_Double_do,Red);` |
| 40 | 2698 | 8 / 8 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),Red);` |
| 41 | 2750 | 20 / 20 | 43 | possible loss of data due to type conversion | `OrderDelete(LR_Temp091_Long_lo,Green);` |
| 42 | 2750 | 8 / 8 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(LR_Temp091_Long_lo,Green);` |
| 43 | 2783 | 20 / 20 | 43 | possible loss of data due to type conversion | `OrderDelete(LR_Temp098_Long_lo,Green);` |
| 44 | 2783 | 8 / 8 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(LR_Temp098_Long_lo,Green);` |
| 45 | 2866 | 17 / 27 | 43 | possible loss of data due to type conversion | `LR_Temp111_Long_lo = LR_Global198_Double_do_Array[LR_Temp110_Int_in][0];` |
| 46 | 2940 | 42 / 59 | 43 | possible loss of data due to type conversion | `LR_Global198_Double_do_Array[LR_Temp003_Int_in][0] = LR_Temp002_Long_lo;` |
| 47 | 2962 | 50 / 67 | 43 | possible loss of data due to type conversion | `LR_Global198_Double_do_Array[LR_Temp006_Int_in][0] = LR_Temp005_Long_lo;` |
| 48 | 2984 | 40 / 57 | 43 | possible loss of data due to type conversion | `LR_Global198_Double_do_Array[LR_Temp009_Int_in][0] = LR_Temp008_Long_lo;` |
| 49 | 3006 | 47 / 63 | 43 | possible loss of data due to type conversion | `LR_Global198_Double_do_Array[LR_Temp012_Int_in][0] = LR_Temp011_Long_lo;` |
| 50 | 3075 | 8 / 8 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),Green);` |
| 51 | 3089 | 8 / 8 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),Green);` |
| 52 | 3121 | 6 / 6 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),Green);` |
| 53 | 3134 | 4 / 4 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),Green);` |
| 54 | 3249 | 21 / 28 | 43 | possible loss of data due to type conversion | `LR_Global145_Int_in = LR_Global385_Int_in / (MaxAllowedDD / 100.0) ;` |
| 55 | 3253 | 21 / 28 | 43 | possible loss of data due to type conversion | `LR_Global145_Int_in = LR_Global386_Int_in / (MaxAllowedDD / 100.0) ;` |
| 56 | 3257 | 21 / 28 | 43 | possible loss of data due to type conversion | `LR_Global145_Int_in = LR_Global387_Int_in / (MaxAllowedDD / 100.0) ;` |
| 57 | 3261 | 21 / 28 | 43 | possible loss of data due to type conversion | `LR_Global145_Int_in = LR_Global388_Int_in / (MaxAllowedDD / 100.0) ;` |
| 58 | 3265 | 21 / 28 | 43 | possible loss of data due to type conversion | `LR_Global145_Int_in = LR_Global389_Int_in / (MaxAllowedDD / 100.0) ;` |
| 59 | 3611 | 6 / 6 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),Red);` |
| 60 | 3632 | 6 / 6 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 61 | 3640 | 8 / 8 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 62 | 3661 | 4 / 4 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 63 | 3668 | 4 / 4 | 83 | return value of 'OrderDelete' should be checked | `OrderDelete(OrderTicket(),0xFFFFFFFF);` |
| 64 | 3826 | 16 / 26 | 43 | possible loss of data due to type conversion | `LR_Temp014_Int_in = AccountInfoInteger(ACCOUNT_LIMIT_ORDERS);` |
| 65 | 3863 | 28 / 38 | 43 | possible loss of data due to type conversion | `LR_Temp016_Int_in = LR_Global038_Double_do * LR_NormalizedPriceUnit;` |
| 66 | 3885 | 49 / 65 | 43 | possible loss of data due to type conversion | `LR_Global198_Double_do_Array[LR_Temp019_Int_in][0] = LR_Temp018_Long_lo;` |
| 67 | 4052 | 16 / 26 | 43 | possible loss of data due to type conversion | `LR_Temp014_Int_in = AccountInfoInteger(ACCOUNT_LIMIT_ORDERS);` |
| 68 | 4089 | 28 / 38 | 43 | possible loss of data due to type conversion | `LR_Temp016_Int_in = LR_Global038_Double_do * LR_NormalizedPriceUnit;` |
| 69 | 4111 | 49 / 65 | 43 | possible loss of data due to type conversion | `LR_Global198_Double_do_Array[LR_Temp019_Int_in][0] = LR_Temp018_Long_lo;` |
| 70 | 4222 | 22 / 22 | 43 | possible loss of data due to type conversion | `OrderModify(LR_Local009_Long_lo,LR_Local010_Double_do,LR_Local007_Double_do,LR_Local008_Double_do,0,Green);` |
| 71 | 4222 | 10 / 10 | 83 | return value of 'OrderModify' should be checked | `OrderModify(LR_Local009_Long_lo,LR_Local010_Double_do,LR_Local007_Double_do,LR_Local008_Double_do,0,Green);` |
| 72 | 4227 | 22 / 22 | 43 | possible loss of data due to type conversion | `OrderModify(LR_Local009_Long_lo,LR_Local010_Double_do,LR_Local007_Double_do,LR_Local008_Double_do,0,Green);` |
| 73 | 4227 | 10 / 10 | 83 | return value of 'OrderModify' should be checked | `OrderModify(LR_Local009_Long_lo,LR_Local010_Double_do,LR_Local007_Double_do,LR_Local008_Double_do,0,Green);` |
| 74 | 4235 | 22 / 22 | 43 | possible loss of data due to type conversion | `OrderModify(LR_Local009_Long_lo,LR_Local010_Double_do,LR_Local007_Double_do,LR_Local008_Double_do,0,Green);` |
| 75 | 4235 | 10 / 10 | 83 | return value of 'OrderModify' should be checked | `OrderModify(LR_Local009_Long_lo,LR_Local010_Double_do,LR_Local007_Double_do,LR_Local008_Double_do,0,Green);` |
| 76 | 4240 | 22 / 22 | 43 | possible loss of data due to type conversion | `OrderModify(LR_Local009_Long_lo,LR_Local010_Double_do,LR_Local007_Double_do,LR_Local008_Double_do,0,Green);` |
| 77 | 4240 | 10 / 10 | 83 | return value of 'OrderModify' should be checked | `OrderModify(LR_Local009_Long_lo,LR_Local010_Double_do,LR_Local007_Double_do,LR_Local008_Double_do,0,Green);` |
| 78 | 4244 | 21 / 21 | 43 | possible loss of data due to type conversion | `OrderClose(LR_Local009_Long_lo,LR_Local012_Double_do,MarketInfo(LR_CurrentSymbol,MODE_BID),0,Red);` |
| 79 | 4244 | 10 / 10 | 83 | return value of 'OrderClose' should be checked | `OrderClose(LR_Local009_Long_lo,LR_Local012_Double_do,MarketInfo(LR_CurrentSymbol,MODE_BID),0,Red);` |
| 80 | 4249 | 21 / 21 | 43 | possible loss of data due to type conversion | `OrderClose(LR_Local009_Long_lo,LR_Local012_Double_do,MarketInfo(LR_CurrentSymbol,MODE_BID),0,Red);` |
| 81 | 4249 | 10 / 10 | 83 | return value of 'OrderClose' should be checked | `OrderClose(LR_Local009_Long_lo,LR_Local012_Double_do,MarketInfo(LR_CurrentSymbol,MODE_BID),0,Red);` |
| 82 | 4254 | 21 / 21 | 43 | possible loss of data due to type conversion | `OrderClose(LR_Local009_Long_lo,LR_Local012_Double_do,MarketInfo(LR_CurrentSymbol,MODE_BID),0,Red);` |
| 83 | 4254 | 10 / 10 | 83 | return value of 'OrderClose' should be checked | `OrderClose(LR_Local009_Long_lo,LR_Local012_Double_do,MarketInfo(LR_CurrentSymbol,MODE_BID),0,Red);` |
| 84 | 4259 | 21 / 21 | 43 | possible loss of data due to type conversion | `OrderClose(LR_Local009_Long_lo,LR_Local012_Double_do,MarketInfo(LR_CurrentSymbol,MODE_BID),0,Red);` |
| 85 | 4259 | 10 / 10 | 83 | return value of 'OrderClose' should be checked | `OrderClose(LR_Local009_Long_lo,LR_Local012_Double_do,MarketInfo(LR_CurrentSymbol,MODE_BID),0,Red);` |
| 86 | 4264 | 21 / 21 | 43 | possible loss of data due to type conversion | `OrderClose(LR_Local009_Long_lo,LR_Local012_Double_do,MarketInfo(LR_CurrentSymbol,MODE_BID),0,Red);` |
| 87 | 4264 | 10 / 10 | 83 | return value of 'OrderClose' should be checked | `OrderClose(LR_Local009_Long_lo,LR_Local012_Double_do,MarketInfo(LR_CurrentSymbol,MODE_BID),0,Red);` |
| 88 | 4290 | 46 / 63 | 43 | possible loss of data due to type conversion | `LR_Global198_Double_do_Array[LR_Temp007_Int_in][0] = LR_Temp006_Long_lo;` |
| 89 | 4323 | 22 / 22 | 43 | possible loss of data due to type conversion | `OrderModify(LR_Local009_Long_lo,LR_Local010_Double_do,LR_Local007_Double_do,LR_Local008_Double_do,0,0xFFFFFFFF);` |
| 90 | 4323 | 10 / 10 | 83 | return value of 'OrderModify' should be checked | `OrderModify(LR_Local009_Long_lo,LR_Local010_Double_do,LR_Local007_Double_do,LR_Local008_Double_do,0,0xFFFFFFFF);` |
| 91 | 4328 | 82 / 85 | 43 | possible loss of data due to type conversion | `OrderClose(OrderTicket(),OrderLots(),MarketInfo(LR_CurrentSymbol,MODE_BID),LR_CurrentSpreadPrice,Red);` |
| 92 | 4328 | 10 / 10 | 83 | return value of 'OrderClose' should be checked | `OrderClose(OrderTicket(),OrderLots(),MarketInfo(LR_CurrentSymbol,MODE_BID),LR_CurrentSpreadPrice,Red);` |
| 93 | 4378 | 92 / 95 | 43 | possible loss of data due to type conversion | `OrderClose(OrderTicket(),OrderLots(),MarketInfo(LR_CurrentSymbol,MODE_BID),LR_Global038_Double_do,Red);` |
| 94 | 4378 | 20 / 20 | 83 | return value of 'OrderClose' should be checked | `OrderClose(OrderTicket(),OrderLots(),MarketInfo(LR_CurrentSymbol,MODE_BID),LR_Global038_Double_do,Red);` |
| 95 | 4381 | 90 / 93 | 43 | possible loss of data due to type conversion | `OrderClose(OrderTicket(),OrderLots(),MarketInfo(LR_CurrentSymbol,MODE_ASK),LR_Global038_Double_do,Red);` |
| 96 | 4381 | 18 / 18 | 83 | return value of 'OrderClose' should be checked | `OrderClose(OrderTicket(),OrderLots(),MarketInfo(LR_CurrentSymbol,MODE_ASK),LR_Global038_Double_do,Red);` |
| 97 | 4412 | 20 / 20 | 83 | return value of 'OrderClose' should be checked | `OrderClose(OrderTicket(),OrderLots(),MarketInfo(LR_CurrentSymbol,MODE_BID),3,Red);` |
| 98 | 4420 | 92 / 95 | 43 | possible loss of data due to type conversion | `OrderClose(OrderTicket(),OrderLots(),MarketInfo(LR_CurrentSymbol,MODE_BID),LR_Global038_Double_do,Red);` |
| 99 | 4420 | 20 / 20 | 83 | return value of 'OrderClose' should be checked | `OrderClose(OrderTicket(),OrderLots(),MarketInfo(LR_CurrentSymbol,MODE_BID),LR_Global038_Double_do,Red);` |
| 100 | 4423 | 90 / 93 | 43 | possible loss of data due to type conversion | `OrderClose(OrderTicket(),OrderLots(),MarketInfo(LR_CurrentSymbol,MODE_ASK),LR_Global038_Double_do,Red);` |
