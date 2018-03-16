import java.io.BufferedReader;
import java.io.FileReader;


import weka.classifiers.Classifier;
import weka.classifiers.Evaluation;
import weka.classifiers.evaluation.output.prediction.CSV;
import weka.classifiers.functions.SMO;
import weka.core.Instances;
import weka.filters.Filter;
import weka.filters.unsupervised.attribute.Remove;


public class Weka {
	
	public static void buildClassifier(String trainFile, String modelFile) throws Exception {

		 Classifier cls = new SMO();
		
		 Instances inst = new Instances(
		                    new BufferedReader(
		                      new FileReader(trainFile)));
		 inst.setClassIndex(inst.numAttributes() - 1);
		 cls.buildClassifier(inst);
		 
		 // serialize model
		 weka.core.SerializationHelper.write(modelFile, cls);
	}
	
	public static void classify(String trainFile, String testFile, String modelFile) throws Exception {

		// deserialize model
		Classifier cls = (Classifier) weka.core.SerializationHelper.read(modelFile);
		 
		 // train
		Instances train = new Instances(
		                   new BufferedReader(
		                     new FileReader(trainFile)));
		train.setClassIndex(train.numAttributes() - 1);
		 

		 // test
		Instances test = new Instances(
		                   new BufferedReader(
		                    new FileReader(testFile)));
		 
		String[] options = new String[2];
		options[0] = "-R";                                    // "range"
		options[1] = "1";                                     // first attribute
		Remove remove = new Remove();                         // new instance of filter
		remove.setOptions(options);                           // set options
		remove.setInputFormat(test);                          // inform filter about dataset **AFTER** setting options
		Instances newTest = Filter.useFilter(test, remove);   // apply filter	 
		 
		newTest.setClassIndex(newTest.numAttributes() - 1);

		// evaluate classifier and print some statistics
		Evaluation eval = new Evaluation(train);

		StringBuffer Buffer = new StringBuffer();
		CSV plainText = new CSV();
		plainText.setHeader(train);
		plainText.setBuffer(Buffer);		 
		eval.evaluateModel(cls, newTest,plainText);

		System.out.printf("True positives: %.6f\tFalse positives: %.6f\tTrue negatives: %.6f\tFalse negatives: %.6f\n", 
				 		eval.weightedTruePositiveRate(), eval.weightedFalsePositiveRate(), eval.weightedTrueNegativeRate(), eval.weightedFalseNegativeRate());
	
		System.out.printf("Precision: %.6f\tRecall: %.6f\tF1-score: %.6f\n", 
				 		eval.weightedPrecision(), eval.weightedRecall(), eval.weightedFMeasure());
		
		BufferedReader in = new BufferedReader(new FileReader("eval_id.txt"));
		String line;
		int i = 0;
		String[] result = Buffer.toString().split("\n"); 
		for (i = 0; (i < 988) && ((line = in.readLine()) != null); i++) {
			String[] temp = result[i].split(",");
			System.out.println(line + "\t"+temp[2].substring(2));
		}
		in.close();
	}

	public static void main(String[] args) throws Exception {
		buildClassifier("p3train.arff", "weather_java_j48.model");
		classify("p3train.arff", "p3eval.arff", "weather_java_j48.model");
	}
}
