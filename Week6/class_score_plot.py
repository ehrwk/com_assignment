import glob, csv
import matplotlib.pyplot as plt

def read_data(filename):
    files = glob.glob(filename)
    all_data = []
    for file in files:
        with open(file, 'r') as f:     
            csv_reader = csv.reader(f) 
            data = []
            for line in csv_reader:
                if line and not line[0].strip().startswith('#'): 
                    data.append([int(val) for val in line])      
            all_data = all_data + data                           

if __name__ == '__main__':
   
    class_kr = read_data('data/class_score_kr.csv')
    class_en = read_data('data/class_score_en.csv')

    
    midtm_kr = [row[0] for row in class_kr]
    final_kr = [row[1] for row in class_kr]
    total_kr = [row[0] * 40 / 125 + row[1] * 60 / 100 for row in class_kr]
    midtm_en = [row[0] for row in class_en]
    final_en = [row[1] for row in class_en]
    total_en = [row[0] * 40 / 125 + row[1] * 60 / 100 for row in class_en]

    
    plt.figure()
    plt.plot(midtm_kr, final_kr, 'r.' , label = 'Korean')
    plt.plot(midtm_en, final_en, 'b+' , label = 'English')
    plt.xlabel('Midterm scores')
    plt.ylabel('Final scores')
    plt.axis([0, 125, 0, 100])
    plt.grid()
    plt.legend()

    
    plt.figure() 
    plt.hist(total_kr, range = (0, 100), bins = 20, color = 'r', label = 'Korean') 
    plt.hist(total_en, range = (0, 100), bins = 20, color = 'b', alpha = 0.5, label = 'English')
    plt.xlabel('Total Score')
    plt.ylabel('The number of students')
    plt.xlim(0, 100)
    plt.legend()