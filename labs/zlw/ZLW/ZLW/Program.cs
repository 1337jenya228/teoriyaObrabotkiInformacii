StreamReader sr = new StreamReader("C:\\Users\\Evgeniy\\PycharmProjects\\teoriyaObrabotkiInformacii\\labs\\zlw\\zlw.txt");
string line = sr.ReadLine();
if (line == null)
{
    line = "Tut pusto";
}
Console.WriteLine(line);
sr.Close();
int count = 0;
string[,] kod = new string[count + 1, 5];
kod[0, 0] = "0";
kod[0, 1] = "esc";
kod[0, 2] = "-";
kod[0, 3] = "-";
kod[0, 4] = "-";
int j, i;
int allcount = 0;
for (i = 0; i < line.Count(); i++)
{
    string slovar = "";
    int check = 1;
    int nomer_slova = 0;
    while (check != 0)
    {
        check = 0;
        slovar += Convert.ToString(line[i]);
        for (j = 0; j < count + 1; j++)
        {
            if (slovar == kod[j, 1])
            {
                check++;
                nomer_slova = j;
            }
        }
        if ((check == 0) || i == line.Length - 1)
        {
            count++;
            kod = Resize(kod, count);
            kod[count, 0] = Convert.ToString(count);
            kod[count, 1] = slovar;
            if ((nomer_slova == j - 1) && (nomer_slova != 0))
            {
                kod[count, 2] = kod[count - 1, 2];
                if ((int)(Math.Log2(count - 1) + 0.99) == (int)(Math.Log2(count - 2) + 0.99))
                {
                    kod[count, 3] = kod[count - 1, 3];
                    kod[count, 4] = kod[count - 1, 4];
                }
                else
                {
                    kod[count, 3] = "0" + kod[count - 1, 3];
                    kod[count, 4] = Convert.ToString(Convert.ToInt32(kod[count - 1, 4]) + 1);
                }
                allcount += Convert.ToInt32(kod[count, 4]);
                if ((i != line.Length - 1) || (check == 0))
                {
                    i--;
                }
            }
            else
            {
                kod[count, 2] = Convert.ToString(nomer_slova);
                if (slovar.Length == 1)
                {
                    if (count == 1)
                    {
                        kod[count, 3] = $"bin({slovar})";
                        kod[count, 4] = "8";
                        allcount += 8;
                    }
                    else
                    {
                        int kol_vo_null = (int)(Math.Log2(count - 1) + 0.99);
                        string add_null = $"bin({slovar})";
                        for (j = 0; j < kol_vo_null; j++)
                        {
                            add_null = "0" + add_null;
                        }
                        kod[count, 3] = add_null;
                        kod[count, 4] = Convert.ToString(kol_vo_null + 8);
                        allcount += kol_vo_null + 8;
                    }
                }
                else
                {
                    int kol_vo_null = (int)(Math.Log2(count - 1) + 0.99);
                    kod[count, 3] = create_kod_simv(kol_vo_null, nomer_slova);
                    kod[count, 4] = Convert.ToString(kol_vo_null);
                    allcount += kol_vo_null;
                    if ((i != line.Length - 1) || (check == 0))
                    {
                        i--;
                    }
                }
            }
            check = 0;
        }
        else
        {
            i++;
        }
    }
}



Console.WriteLine("Шаг\tСловарь\tНомер слова\tКодовые символы\tЗатраты бит");
for (i = 0; i < count + 1; i++)
{
    Console.WriteLine(kod[i, 0] + "\t" + kod[i, 1] + "\t" + kod[i, 2] + "\t\t" + kod[i, 3] + "\t\t" + kod[i, 4]);
}
Console.WriteLine($"Общие затраты бит: {allcount}");


string create_kod_simv(int kol_vo_chisel, int chislo)
{
    string new_chislo = "";
    while (chislo != 0)
    {
        new_chislo = Convert.ToString(chislo % 2) + new_chislo;
        chislo /= 2;
    }
    while (new_chislo.Length != kol_vo_chisel)
    {
        new_chislo = "0" + new_chislo;
    }
    return new_chislo;
}

string[,] Resize(string[,] kod, int count)
{
    string[,] new_kod = new string[count + 1, 5];
    for (int i = 0; i < count; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            new_kod[i, j] = kod[i, j];
        }
    }
    return new_kod;
}